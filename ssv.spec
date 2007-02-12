Summary:	Session Sniffer - help in monitoring users behavior
Summary(pl.UTF-8):   Session Sniffer - pomoc przy monitorowaniu zachowania użytkowników
Name:		ssv
Version:	1.1
Release:	1
Group:		Networking/Admin
License:	GPL (?)
Source0:	http://www.team.com.pl/arkth/%{name}1-1.tar.gz
# Source0-md5:	4ed69bf54b13f5d7ed44d6d3bf807ef8
URL:		http://www.team.com.pl/arkth/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Session Sniffer is a tool to help in monitoring users behavior. It can
be also usefull in gathering information about attacker.

%description -l pl.UTF-8
Session Sniffer jest narzędziem pomocnym przy monitorowaniu zachowania
użytkowników. Może być także pomocne przy znajdowaniu informacji o
intruzach.

%prep
%setup -q -n ss

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o ss ss.c


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install ss $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* Copyright
%attr(755,root,root) %{_sbindir}/*
