from django import template
register = template.Library()

@register.inclusion_tag("addons_admin.html")
def addons_admin(path):
	script = ""
	if path == "/tours/tours/add/":
	
		script += """
				
			"""
	return { "path": path, "script" : script }
		
@register.inclusion_tag("addons_admin_script.html")
def addons_admin_script(path):
	script = ""

	settings = {
		"dynamic_date": False
	}
	
	if path == "/tours/tours/add/":
		settings["dynamic_date"] = True
		script += """
				
			"""

	return { "settings": settings, "path": path, "script" : script }
