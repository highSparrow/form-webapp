# CS 41 Form Web App Template

[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/stanfordpython/form-webapp.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/stanfordpython/form-webapp/context:python)
[![Language grade: JavaScript](https://img.shields.io/lgtm/grade/javascript/g/stanfordpython/form-webapp.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/stanfordpython/form-webapp/context:javascript)

## Overview
This project is a framework for a light-weight, customizable web-app which presents as a form where the user can input information which will be processed by a Python function. It's designed for CS 41 students to be able to add a front-end to their applications, where the input is simple.

## Disclosure
I threw this together in like two hours. It's *far* from perfect, not well documented, and is prone to breaking suddenly and gracelessly.

Good luck! Use Piazza if you need it!.

## Setting Up
To set up this project, the following variables need to be configured:

```
APP_TITLE (app.py)            -- The title of the application, appears at the top of the page.
AUTHORS (app.py)              -- The project authors, appear below the app title.
FORM_DESCRIPTION (app.py)     -- A multi-line description of the form, explaining each field to the user (optional).
FORM_SPECIFICATION (app.py)   -- A dictionary that tells the application how to render a form.
process (process/__init__.py) -- The function to process the results of the form.
```

### Form Specification
The form specification is a little involved, so I'll explain how it works in more detail. Modify the `FORM_SPECIFICATION` variable to be a dictionary of the form

```python
{
	'field_name': ('Field Label', field_type),
	...
}
```

Every entry in the dictionary represents an input from your form. `field_name` will eventually be the variable name of that input in your process function. *This means it should be a valid Python variable name*. The label will be displayed to the user, above the input control, as a description of that input. The `field_type` is one of:

```
FormInputs.STRING   -- A string input area.
FormInputs.TEXTAREA -- A textarea for large string inputs.
FormInputs.NUMERIC  -- A numeric input area.
FormInputs.FILE     -- A file upload input.
```

or an iterable of objects. For example, if `field_type` is `FormInputs.TEXTAREA`, the program will render a textarea where form users can type a multi-line string.

If you provide an iterable of objects as the `field_type`, the program will render a multi-option selctor, where the user can choose one of the objects in the iterable.

### The `process` Function
After you set up the form, you can modify the `process` function. `process` will be called by unpacking the form inputs into the function. So, if you have a form input field whose name is `size`, and the user enters `7`, then the `process` function will be called with `size=7`.

This function is defined in a sub-folder of the project so that you can copy the rest of your project into that folder and the import structure should behave as expected.

By default, `process` should return a string, which will be displayed to the user. You can modify this however you'd like. 

For example, if you wanted to return a string and a plot, you can return a tuple containing a string and base64 data for the image of a plot (see [this tutorial](https://matplotlib.org/faq/howto_faq.html#how-to-use-matplotlib-in-a-web-application-server)). Then, you should modify `templates/index.html` so that instead of rendering:

```html
<div class="alert alert-info" role="alert">
    {{ msg }}
</div>
```

the application renders:

```html
<div class="alert alert-info" role="alert">
    {{ msg[0] }}
</div>
```

(since `msg` will be a tuple, where `msg[0]` is the string message).

You can render the image data by adding 

```html
<img src='data:image/png;base64,{{ msg[1] }}'/>
```

somewhere in `templates/index.html`.

### A Note on Files
If your form requests that the user upload a file as input, the file will be uploaded to the `uploads/` folder. Your script will be provided a string path to the file.

For example, if you wanted the user to upload a file containing GIS data, and you named the variable `gis`, then `process` would be called with `gis='uploads/filename.gis'`. You can access the data by opening the file in the standard way (`with open(gis) as f:`).

> With &#129412;s by @psarin and @coopermj
