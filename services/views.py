from django.shortcuts import render

def service_list(request):
    services = (
        {'id': 1,
         'name': 'Project Name',
         'description': 'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, interdum justo suscipit id.',
         'image': 'img/desk.jpg'            
        },
        {'id': 2,
         'name': 'Project Name',
         'description': 'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, interdum justo suscipit id.',
         'image': 'img/building.jpg'            
        },
        {'id': 3,
         'name': 'Project Name',
         'description': 'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, interdum justo suscipit id.',
         'image': 'img/loft.jpg'            
        },
        {'id': 4,
         'name': 'Project Name',
         'description': 'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, interdum justo suscipit id.',
         'image': 'img/minibus.jpeg'            
        }
    )
    return render(request,'services/services.html',{'services': services})