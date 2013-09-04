CodeCamp = Ember.Application.create({
  rootElement: '#ember'
});

CodeCamp.Session = DS.Model.extend({
  name: DS.attr('string'),
  room: DS.attr('string'),
  tags: DS.hasMany('tag', {async: true }),
  speakers: DS.hasMany('speaker', { async: true }),
  ratings: DS.hasMany('rating', { async: true })
});

CodeCamp.Speaker = DS.Model.extend({
    name: DS.attr('string'),
    location: DS.attr('string'),
    association: DS.belongsTo('association'),
    personas: DS.hasMany('persona', { async: true }),
    session: DS.belongsTo('session'),
    zidentity: DS.belongsTo('user')
});

CodeCamp.Speaker.reopen({
    becameError: function(errors) {
        var model = this.constructor.typeKey;
        alert("operation failed for model: " + model);
    }
});

CodeCamp.Tag = DS.Model.extend({
  description: DS.attr('string')
});

CodeCamp.Rating = DS.Model.extend({
  score: DS.attr('number'),
  feedback: DS.attr('string'),
  session: DS.belongsTo('session')
});

CodeCamp.Association = DS.Model.extend({
  name: DS.attr('string'),
  speakers: DS.hasMany('speaker', { async: true})
});

CodeCamp.User = DS.Model.extend({
    username: DS.attr('string'),
    aliases: DS.hasMany('speaker', { async: true})
});

CodeCamp.Company = DS.Model.extend({
    name: DS.attr('string'),
    sponsors: DS.hasMany('sponsor', { async: true}),
    persona: DS.belongsTo('persona')
});

CodeCamp.Persona = DS.Model.extend({
    nickname: DS.attr('string'),
    speaker: DS.belongsTo('speaker'),
    company: DS.belongsTo('company')
});

CodeCamp.Sponsor = DS.Model.extend({
    name: DS.attr('string'),
    company: DS.belongsTo('company')
});

CodeCamp.Router.map(function() {
  this.route("sessions", { path : "/" });
  this.route("associations", { path : "/associations" });
  this.route("speakers", { path : "/speakers" });
  this.route("session", { path : "/session/:session_id" });
  this.route("speaker", { path : "/speaker/:speaker_id" });
});

CodeCamp.SessionsRoute = Ember.Route.extend({
  model: function() {
    return this.store.find('session');
  }
});

CodeCamp.SpeakersRoute = Ember.Route.extend({
  model: function() {
      return this.store.find('speaker', {name: 'Joel Taddei'});
    }
});

CodeCamp.AssociationsRoute = Ember.Route.extend({
  model: function() {
      return this.store.find('association');
    }
});

CodeCamp.SpeakerController = Ember.ObjectController.extend({
  actions: {
      updateSpeaker: function(model) {
          model.save();
      }
  }
});

CodeCamp.SessionController = Ember.ObjectController.extend({
  actions: {
      addSpeaker: function(session) {
          //var user = CodeCamp.User.find(1);
          //var association = CodeCamp.Association.find(1);
          var name = this.get('speaker');
          var location = this.get('location');
          var speaker = {name: name, location: location, session: session};
          this.store.createRecord('speaker', speaker).save();
      },
      addRating: function(event) {
        var score = this.get('score');
        var feedback = this.get('feedback');
        if (score === undefined || feedback === undefined || score.trim() === "" || feedback.trim() === "") {
          return;
        }
        var rating = { score: score, feedback: feedback, session: event};
        this.store.createRecord('rating', rating).save();
        //event.get('ratings').createRecord('rating', rating).save();
        //won't update the template currently :(
        this.set('score', '');
        this.set('feedback', '');
      },
      deleteRating: function(rating) {
          rating.deleteRecord();
          rating.save();
      }
  }
});

CodeCamp.ApplicationAdapter = DS.DjangoRESTAdapter.extend({
    namespace: 'codecamp'
});
