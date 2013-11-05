module.exports = function(karma) {
    karma.set({
        basePath: 'codecamp/static/script',

        files: [
          "vendor/jquery-1.9.1.js",
          "vendor/handlebars-1.0.0.js",
          "vendor/ember.js",
          "vendor/ember-data.js",
          "vendor/adapter.js",
          "vendor/jquery.mockjax.js",
          "app/codecamp.js",
          "tests/*.js",
          "app/templates/*.handlebars"
        ],

        logLevel: karma.LOG_ERROR,
        browsers: ['PhantomJS'],
        singleRun: true,
        autoWatch: false,

        frameworks: ["qunit"],

        plugins: [
            'karma-qunit',
            'karma-chrome-launcher',
            'karma-ember-preprocessor',
            'karma-phantomjs-launcher'
        ],

        preprocessors: {
            "**/*.handlebars": 'ember'
        }
    });
};
