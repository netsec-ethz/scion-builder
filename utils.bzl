# Generate scion.preinst script, with __DEB_VERSION__ replaced
def substitute_deb_version(name, src, version, visibility=None):
  native.genrule(
    name = name,
    srcs = [src],
    outs = ["tmp" + name + "/" + src],
    cmd = "sed 's/__DEB_VERSION__/" + version + "/' \"$<\" > \"$@\"",
    visibility = visibility,
  )
