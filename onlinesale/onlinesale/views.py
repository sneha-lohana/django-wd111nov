from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
  context = {'head':'Home Page', 
    'content':'Welcome to Itvedant Education Private Limited'}
  if request.user.is_authenticated:
    context["user"] = request.user
  return render(request, "home.html", context)

def contact_page(request):
  context = {'head':'Contact Page', 
    'content':'To enroll call now on 9820610877'}
  return render(request, "home.html", context)

def about_page(request):
  context = {'head':'About Page'}
  context['content'] = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Morbi blandit cursus risus at ultrices mi tempus imperdiet nulla. Dolor purus non enim praesent elementum facilisis leo. Posuere urna nec tincidunt praesent semper feugiat nibh sed. Habitant morbi tristique senectus et netus. Egestas egestas fringilla phasellus faucibus scelerisque eleifend donec pretium. Massa id neque aliquam vestibulum morbi blandit cursus risus. Interdum velit euismod in pellentesque massa. Tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum. Nulla facilisi morbi tempus iaculis urna id. Hendrerit dolor magna eget est lorem ipsum dolor sit. Nisl suscipit adipiscing bibendum est ultricies. At augue eget arcu dictum. Elit pellentesque habitant morbi tristique senectus et netus. Pretium lectus quam id leo in vitae turpis massa. Dapibus ultrices in iaculis nunc sed augue lacus viverra vitae.

Dictumst vestibulum rhoncus est pellentesque elit ullamcorper dignissim cras. Curabitur vitae nunc sed velit dignissim sodales. Interdum posuere lorem ipsum dolor sit amet consectetur adipiscing elit. Morbi non arcu risus quis. Ligula ullamcorper malesuada proin libero nunc consequat. Feugiat nisl pretium fusce id velit ut tortor pretium. Viverra mauris in aliquam sem fringilla. Duis at consectetur lorem donec massa. Adipiscing elit duis tristique sollicitudin nibh sit. Cras tincidunt lobortis feugiat vivamus at augue eget arcu dictum. Etiam erat velit scelerisque in dictum non consectetur. Tellus in metus vulputate eu scelerisque felis imperdiet. Lectus proin nibh nisl condimentum id venenatis a. Elementum facilisis leo vel fringilla est. Praesent tristique magna sit amet. Placerat vestibulum lectus mauris ultrices eros in cursus. Nunc sed augue lacus viverra vitae congue eu. Varius sit amet mattis vulputate enim nulla aliquet. Ut diam quam nulla porttitor massa id.

Morbi non arcu risus quis varius. Accumsan lacus vel facilisis volutpat est velit. Nisl nunc mi ipsum faucibus vitae. Vestibulum morbi blandit cursus risus at ultrices mi tempus. Senectus et netus et malesuada fames ac turpis egestas sed. Aliquet sagittis id consectetur purus ut faucibus pulvinar elementum. Amet est placerat in egestas. Vel pretium lectus quam id leo in. Aliquam sem fringilla ut morbi tincidunt augue interdum. Tellus orci ac auctor augue mauris augue neque gravida in. Nec nam aliquam sem et tortor consequat id porta. Elementum sagittis vitae et leo. Platea dictumst quisque sagittis purus sit amet volutpat consequat mauris. Mauris sit amet massa vitae tortor condimentum lacinia.

Sociis natoque penatibus et magnis dis. Nulla aliquet porttitor lacus luctus accumsan tortor. Rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras. Neque vitae tempus quam pellentesque nec. Odio morbi quis commodo odio aenean sed adipiscing diam donec. Est sit amet facilisis magna etiam. Varius quam quisque id diam vel quam elementum pulvinar. Dignissim diam quis enim lobortis scelerisque fermentum dui. Maecenas accumsan lacus vel facilisis volutpat est velit egestas dui. In hendrerit gravida rutrum quisque. Pellentesque dignissim enim sit amet venenatis urna.

Sed nisi lacus sed viverra tellus in. Tincidunt nunc pulvinar sapien et ligula ullamcorper malesuada. Orci eu lobortis elementum nibh tellus. Sit amet luctus venenatis lectus magna. Ut consequat semper viverra nam libero justo laoreet sit amet. Lorem mollis aliquam ut porttitor leo a. Vel fringilla est ullamcorper eget. Metus dictum at tempor commodo ullamcorper a lacus vestibulum. Purus semper eget duis at tellus at urna condimentum mattis. Tincidunt arcu non sodales neque sodales ut etiam sit amet. Accumsan in nisl nisi scelerisque eu ultrices vitae auctor eu. At quis risus sed vulputate odio ut enim blandit. Pellentesque elit ullamcorper dignissim cras tincidunt lobortis feugiat. Orci a scelerisque purus semper eget duis at. Ac odio tempor orci dapibus.""" 
  return render(request, "home.html", context)

def home_page2(request):
    _html = """<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body class="text-center">
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
</html>"""
    return HttpResponse(_html)

def home_page1(request):
    return HttpResponse("<h1>Hello World!</h1>")