Summary:	Session Sniffer - help in monitoring users behavior.
Summary(pl):	Session Sniffer - pomoc przy monitorowaniu zachowania u�ytkownik�w
Name:		ssv
Version:	1.1
Release:	1
Group:		Networking/Admin
License:	GPL (?)
Source0:	http://www.team.com.pl/arkth/%{name}1-1.tar.gz
URL:		http://www.team.com.pl/arkth/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Session Sniffer is a tool to help in monitoring users behavior.
It can be also usefull in gathering information about attacker.

%description -l pl
Session Sniffer jest narz�dziem pomocnym przy monitorowaniu 
zachowania u�ytkownik�w. Mo�e by� tak�e pomocne przy znajdowaniu
informacji o intruzach.

%prep
%setup -q -n ss

%build
%{__cc} %{rpmcflags} -o ss ss.c

gzip -9nf README* Copyright

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_sbindir}
install ss $RPM_BUILD_ROOT/%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
