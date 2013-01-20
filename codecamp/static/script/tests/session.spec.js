require('static/script/app/codecamp.js');
require('static/script/tests/local_adapter.js');

describe ("CodeCamp.SessionView Tests", function(){

  var get = Ember.get, set = Ember.set, sut, controller, session, store;

  beforeEach(function(){
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
      store.destroy();
      controller.destroy();
      sut.destroy();
      session.destroy();
    });
    store = null;
    controller = null;
    sut = null;
    session = null;
  });

  it ("form is not valid when score is never set but feedback is legit", function(){
    sut.set('score', undefined);
    sut.set('feedback', 'foo');
    var result = sut.formIsValid();
    expect(result).toEqual(false);
  });

  it ("form is not valid when score is legit but feedback is never set", function(){
    sut.set('score', 'foo');
    sut.set('feedback', undefined);
    var result = sut.formIsValid();
    expect(result).toEqual(false);
  });

  it ("form is not valid when score is empty string but feedback is legit", function(){
    sut.set('score', '');
    sut.set('feedback', 'foo');
    var result = sut.formIsValid();
    expect(result).toEqual(false);
  });

  it ("form is not valid when score is legit but feedback is empty string", function(){
    sut.set('score', 'foo');
    sut.set('feedback', '');
    var result = sut.formIsValid();
    expect(result).toEqual(false);
  });

  it ("form is not valid when score is blank space but feedback is legit", function(){
    sut.set('score', ' ');
    sut.set('feedback', 'foo');
    var result = sut.formIsValid();
    expect(result).toEqual(false);
  });

  it ("form is not valid when score is legit but feedback is blank space", function(){
    sut.set('score', 'foo');
    sut.set('feedback', ' ');
    var result = sut.formIsValid();
    expect(result).toEqual(false);
  });

  it ("form is valid when score is legit and feedback is legit", function(){
    sut.set('score', 'foo');
    sut.set('feedback', 'bar');
    var result = sut.formIsValid();
    expect(result).toEqual(true);
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
