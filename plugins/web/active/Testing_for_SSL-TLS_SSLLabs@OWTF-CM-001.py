from framework.dependency_management.dependency_resolver import ServiceLocator
""" 
ACTIVE Plugin for Testing for SSL-TLS from SSLLabs(OWASP-CM-001)
"""

DESCRIPTION = "Active probing for SSL configuration"

def run(PluginInfo):
	#ServiceLocator.get_component("config").Show()
	Content = ServiceLocator.get_component("plugin_helper").CommandDump('Test Command', 'Output', ServiceLocator.get_component("resource").GetResources('ActiveSSLLabsScan'), PluginInfo, []) # No previous output
	return Content

