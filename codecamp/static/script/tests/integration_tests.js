module('integration tests', {
    setup: function() {
        Ember.run(function() {
            CodeCamp.reset();
            CodeCamp.deferReadiness();
        });
    },
    teardown: function() {
        $.mockjaxClear();
    }
});

test('ajax response with 1 session yields table with 1 row', function() {
    var json = [{"id": 1, "name": "foo", "room": "bar", "desc": "test", "speakers": [], "ratings": [], "tags": []}];
    stubEndpointForHttpRequest('/codecamp/sessions/', json);
    Ember.run(CodeCamp, 'advanceReadiness');
    visit("/").then(function() {
        var rows = find("table tr").length;
        equal(rows, 1, "table had " + rows + " rows");
        var first = $("table tr:eq(0) td:eq(0)").text();
        equal(first, "foo", "first was instead: " + first);
    });
});

test('ajax response with 0 session yields empty table', function() {
    stubEndpointForHttpRequest('/codecamp/sessions/', []);
    Ember.run(CodeCamp, 'advanceReadiness');
    visit("/").then(function() {
        var rows = find("table tr").length;
        equal(rows, 0, "table had " + rows + " rows");
    });
});
