// vue.config.js
if (process.env.NODE_ENV === 'production' || process.env.NODE_ENV === 'staging') {
    module.exports = {
        outputDir: '../../backend/flask-api/dist',
        assetsDir: '../static'
    }
}