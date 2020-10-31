// vue.config.js
if (process.env.NODE_ENV === 'production') {
    module.exports = {
        outputDir: '../../backend/flask-api/dist',
        assetsDir: '../static'
    }
}