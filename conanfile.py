from conans import ConanFile

class ExtraBoolean(ConanFile):
  name = "extra-boolean"
  version = "0.0"
  exports_sources = "src/*"
  no_copy_source = True

  def package(self):
    self.copy("*.h")
