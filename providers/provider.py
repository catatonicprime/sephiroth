from . import AWS, Azure, GCP, OCI

classmap = {
	"aws": AWS,
	"azure": Azure,
	"gcp": GCP,
	"oci": OCI
}

class Provider():
	def __init__(self, provider):
		self.provider = classmap[provider]()

	def get_processed_ranges(self):
		return self.provider.get_processed_ranges()