# Fedora packaging for Scylla

## Getting Started

Prerequisites:

```
dnf install rpmdevtools
```

Build RPM packages with:

```
rpmbuild --undefine=_disable_source_fetch -ba scylla.spec 
```
