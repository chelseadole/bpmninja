const webpack = require('webpack');

const config = {
    entry: {
        'index': __dirname + 'js/index.jsx',
        'play': __dirname + 'js/play.jsx'
    }
    output: {
        path: __dirname + '/dist', 
        filename: '[name].js', 
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },2
};
module.exports = config;