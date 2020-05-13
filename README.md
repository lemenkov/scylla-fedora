# Fedora packaging for Scylla

## Getting Started

Prerequisites:

```
dnf install rpmdevtools dnf-plugins-core
```

Build RPM packages with:

```
dnf builddep scylla.spec
rpmbuild --undefine=_disable_source_fetch -ba scylla.spec 
```
