require('static/script/app/codecamp.js');

describe ("CodeCamp.SessionView Tests", function(){

  var sut, controller, session, event;

  beforeEach(function(){
    sut = CodeCamp.SessionView.create();
    controller = new Object({addRating:function(){}});
    sut.set("controller", controller);
    session = CodeCamp.Session.createRecord();
    event = {'context': session};
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

  it ("will not reset any form input when form is not valid", function(){
    spyOn(sut, 'formIsValid').andReturn(false);
    spyOn(sut, 'buildRatingFromInputs');
    sut.set('score', ' ');
    sut.set('feedback', 'foo');
    sut.addRating(event);
    expect(sut.get('score')).toEqual(' ');
    expect(sut.get('feedback')).toEqual('foo');
  });

  it ("will reset each form input when form is valid", function(){
    spyOn(sut, 'formIsValid').andReturn(true);
    spyOn(sut, 'buildRatingFromInputs').andReturn(new Object());
    sut.set('score', '1234');
    sut.set('feedback', 'abcd');
    sut.addRating(event);
    expect(sut.get('score')).toEqual('');
    expect(sut.get('feedback')).toEqual('');
  });

  it ("will not invoke addRating on the controller when form is not valid", function(){
    spyOn(sut, 'formIsValid').andReturn(false);
    var addSpy = spyOn(controller, 'addRating');
    sut.addRating(event);
    expect(addSpy).not.toHaveBeenCalledWith(jasmine.any(Object));
  });

  it ("will invoke addRating on the controller when form is valid", function(){
    spyOn(sut, 'formIsValid').andReturn(true);
    var addSpy = spyOn(controller, 'addRating')
    sut.addRating(event);
    expect(addSpy).toHaveBeenCalledWith(jasmine.any(Object));
  });

  it ("invokes addRating on the controller with a complete rating object when form is valid", function(){
    spyOn(sut, 'formIsValid').andReturn(true);
    sut.set('score', '1234');
    sut.set('feedback', 'abcd');
    var addSpy = spyOn(controller, 'addRating')
    sut.addRating(event);
    expect(addSpy.argsForCall[0][0].get('session')).toBe(session);
    expect(addSpy.argsForCall[0][0].get('score')).toEqual('1234');
    expect(addSpy.argsForCall[0][0].get('feedback')).toEqual('abcd');
  });

});

describe ("CodeCamp.SessionController Tests", function(){

  var sut, store, rating, session;

  beforeEach(function(){
    sut = CodeCamp.SessionController.create();
    store = new Object({commit:function(){}});
    session = CodeCamp.Session.createRecord({name:'foo', 'ratings':[]});
    sut.set('content', session);
    sut.set("store", store);
    rating = CodeCamp.Rating.createRecord();
  });

  it ("will invoke commit on the store", function(){
    var commitSpy = spyOn(store, 'commit')
    sut.addRating(rating);
    expect(commitSpy).toHaveBeenCalledWith();
  });

});
