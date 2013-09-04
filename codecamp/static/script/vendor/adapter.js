var get = Ember.get, set = Ember.set, isNone = Ember.isNone;

DS.DjangoRESTSerializer = DS.JSONSerializer.extend({

    init: function() {
        this._super.apply(this, arguments);
    },

});

DS.DjangoRESTAdapter = DS.RESTAdapter.extend({
    defaultSerializer: "DS/djangoREST",

    createRecord: function(store, type, record) {
      var data = store.serializerFor(type.typeKey).serialize(record);
      return this.ajax(this.buildURL(type.typeKey), "POST", { data: data });
    },

    updateRecord: function(store, type, record) {
      var data = store.serializerFor(type.typeKey).serialize(record);
      var id = get(record, 'id');
      return this.ajax(this.buildURL(type.typeKey, id), "PUT", { data: data });
    },

    findMany: function(store, type, ids, parent) {
        var adapter, root, url;
        adapter = this;

        if (parent) {
            url = this.buildFindManyUrlWithParent(type, parent);
        } else {
            console.log("untested currently")
            console.log("objects w/ multiple parents will hit this");
            url = this.buildURL(type.typeKey);
        }

        return this.ajax(url, "GET");
    },

    ajax: function(url, type, hash) {
      hash = hash || {};
      hash.cache = false;

      return this._super(url, type, hash);
    },

    buildURL: function(type, id) {
        var url = this._super(type, id);

        if (url.charAt(url.length -1) !== '/') {
            url += '/';
        }

        return url;
    },

    buildFindManyUrlWithParent: function(type, parent) {
        var root, url, endpoint, parentValue;

        endpoint = Ember.String.pluralize(type.typeKey);
        parentValue = parent.get('id');
        root = parent.constructor.typeKey;
        url = this.buildURL(root, parentValue);

        return url + endpoint + '/';
    }

});
