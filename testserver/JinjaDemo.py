'''
Created on 30.12.2016

@author: stroeter
'''

import jinja2

def rendertemplate( templateFile, context):
    return jinja2.Environment(loader=jinja2.FileSystemLoader('./templates')).get_template(templateFile).render(context)

     
def jinjaDemo():
    context={'my_string' : "Wheeeee!", 
             'my_list' : [0,1,2,3,4,5]}
    return rendertemplate( "demo_template.html", context )
    
        
    