require('static/script/app/codecamp.js');
require('static/script/tests/local_adapter.js');

describe ("CodeCamp.SessionView Tests", function(){

  var sut, controller, session, store, root, rootElement;

  beforeEach(function(){
    root = $('body').append('<div id="controller-tests" />');
    rootElement = window.CodeCamp.rootElement;
    window.CodeCamp.rootElement = $("#controller-tests");
    store = DS.Store.create({
      revision: 11,
      adapter: DS.LSAdapter.create()
    });
    sut = CodeCamp.SessionView.create();
    controller = CodeCamp.SessionController.create();
    controller.set("store", store);
    sut.set("controller", controller);
    session = CodeCamp.Session.createRecord({ id: 1, name: "First", room: "A", ratings: [], speakers: [], tags: []});
  });

  afterEach(function() {
    Ember.run(function() {
      session.destroy();
      sut.destroy();
      controller.destroy();
      store.destroy();
    });
    session = null;
    sut = null;
    controller = null;
    store = null;
    window.CodeCamp.rootElement = rootElement;
    $("#controller-tests").html('');
  });

  it ("will create rating when form is valid", function(){
    sut.set('score', '1234');
    sut.set('feedback', 'abcd');
    sut.addRating(session);
    var ratings = CodeCamp.Session.find(1).get('ratings');
    var rating = ratings.objectAt(0);
    expect(rating.get('score')).toEqual('1234');
    expect(rating.get('feedback')).toEqual('abcd');
    expect(rating.get('session').get('id')).toEqual(1);
  });

});
