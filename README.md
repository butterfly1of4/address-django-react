# Make a new django project:
Run:
```pip install Django```
```django-admin startproject address_django_react```
```python manage.py migrate```

# Create Front-end App 
Run:
```python manage.py startapp frontend```

# In settings.py:

INSTALLED_APPS = [
  'frontend',
  ...
]

# Create:

## Folders: 
'templates' IN 'frontend' ,
'frontend' in 'templates 

## File:
'frontend/templates/frontend/index.html'

### Add boilerplate info:
// in: index.html 
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Site</title>
</head>
<body>
  <div id="app"></div>
</body>
</html>
```

## Add: 
//in: frontend/views.py
```
from django.shortcuts import render

def index(request):
  return render(request, 'frontend/index.html')
  ```
//in: address_django_react/urls.py
```
from django.urls import include, path

urlpatterns = [
  ...,
  path('', include('frontend.urls'))
]
```

## Create: 
//in: frontend
```urls.py```
### Add:
```
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index)
]
```
## TO TEST: 
```python manage.py runserver```
In: localhost:8000
    - blank screen w/ 'My Site' on tab

# Set up React, Babel, Webpack:

## Install: 
    - Node
    - React
//in: address_django_react (root)
Run:
```npm init -y```
```npm install react react-dom```

# Babel:
## Install:
```npm install --save-dev @babel/core```
//add presets
```npm install --save-dev @babel/preset-env @babel/preset-react```
## Create:
//in: addrerss_django_react(root)
```.babelrc```
## Add:
```{
  "presets": ["@babel/preset-env", "@babel/preset-react"]
}
```
# Webpack:
## Install:
```npm install --save-dev webpack webpack-cli webpack-bundle-tracker@0.4.3 babel-loader css-loader style-loader clean-webpack-plugin```

#### Explanation of dependencies:
webpack is... well, Webpack
webpack-cli allows you to run Webpack commands from the command line
webpack-bundle-tracker is a plugin that writes some stats about the bundle(s) to a JSON file.
babel-loader is a loader that tells Webpack to run Babel on the file before adding it to the bundle.
css-loader and style-loader are loaders that allow you to import .css files into your JavaScript
clean-webpack-plugin is a plugin that deletes old bundles from Webpack's output directory every time a new bundle is created.

## Create:
//in: addrerss_django_react(root)
```webpack.config.js```

## Add:
// in: webpack.config.js
```
const path = require('path')
const BundleTracker = require('webpack-bundle-tracker')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')

module.exports = {
  entry: {
    frontend: './frontend/src/index.js',
  },
  output: {
    path: path.resolve('./frontend/static/frontend/'),
    filename: '[name]-[hash].js',
  },
  plugins: [
    new CleanWebpackPlugin(),
    new BundleTracker({
      path: __dirname,
      filename: './webpack-stats.json',
    }),
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ['babel-loader']
        },
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
}
```

#### Explanation of dependencies:
entry tells Webpack where to start gathering your code
output is where Webpack will put the finished bundle.
plugins tells Webpack which plugins to use
module is where you configure your loaders. Each rule tells Webpack that whenever it comes across a file that matches the test regex, it should use the specified loaders to process it.

## Add:
//in: package.json
``` 
"scripts": {
    "dev": "webpack --config webpack.config.js --watch --mode development",
    "build": "webpack --config webpack.config.js --mode production"
   }
```
#### work with ```npm run dev``` and ```npm run build```

# Bundle to HTML:

## Install:
Run: 
```pip install django-webpack-loader```

## Add:
//in: address_django_react/settings.py
```
(@top)
import os

...
(in)
INSTALLED_APPS = [
  'webpack_loader',
  ...
]

...
(in)
WEBPACK_LOADER = {
  'DEFAULT': {
    'BUNDLE_DIR_NAME': 'frontend/',
    'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json')
  }
}
```
## Add:
//in: fronten/templates/frontend/index.html
<!DOCTYPE html>

----Add this---
+ {% load render_bundle from webpack_loader %} 
-------
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Site</title>
</head>
<body>
  <div id="app"></div>
  -----Add this-----
+ {% render_bundle 'frontend' %} 
---------
</body>
</html>

# Create React App

## Create:
//in frontend folder:

Folder: ```src``` IN `frontend`
File: ```App.js``` IN `src`

In App.js:
```
import React from 'react'

const App = () => {
  return (
    <div>Hello, World!</div>
  )
}

export default App
```
## Create:
//in src folder:
File: ```index.js``` in `src`

In index.js:
```
import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'

ReactDOM.render(
  <App />,
  document.getElementById('app')
)
```

## Run:
//in addrerss_django_react (root)
**Run this firs***
```npm run dev```

//in seperate terminal:
```python manage.py runserver```

## Open:
locahost:8000