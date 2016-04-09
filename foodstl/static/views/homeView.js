var HomeView = Backbone.View.extend({
    el: '#main',

    initialize: function(){
        this.render();
    },

    render: function(){
        var template = _.template($('#template').text());
        this.$el.html(template());
    },

    events: {
        
    }
});
