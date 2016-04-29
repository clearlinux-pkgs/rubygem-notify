#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-notify
Version  : 0.5.2
Release  : 5
URL      : https://rubygems.org/downloads/notify-0.5.2.gem
Source0  : https://rubygems.org/downloads/notify-0.5.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-notify-bin
BuildRequires : ruby
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc

%description
notify
======
"Notify" provides notification functionalities on cross platforms.

%package bin
Summary: bin components for the rubygem-notify package.
Group: Binaries

%description bin
bin components for the rubygem-notify package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n notify-0.5.2
gem spec %{SOURCE0} -l --ruby > rubygem-notify.gemspec

%build
gem build rubygem-notify.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
notify-0.5.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/notify-0.5.2.gem
/usr/lib64/ruby/gems/2.3.0/gems/notify-0.5.2/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/notify-0.5.2/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/notify-0.5.2/README.md
/usr/lib64/ruby/gems/2.3.0/gems/notify-0.5.2/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/notify-0.5.2/VERSION
/usr/lib64/ruby/gems/2.3.0/gems/notify-0.5.2/bin/notify
/usr/lib64/ruby/gems/2.3.0/gems/notify-0.5.2/lib/notify.rb
/usr/lib64/ruby/gems/2.3.0/gems/notify-0.5.2/lib/notify/growlnotify.rb
/usr/lib64/ruby/gems/2.3.0/gems/notify-0.5.2/lib/notify/kdialog.rb
/usr/lib64/ruby/gems/2.3.0/gems/notify-0.5.2/lib/notify/libnotify.rb
/usr/lib64/ruby/gems/2.3.0/gems/notify-0.5.2/lib/notify/notify-send.rb
/usr/lib64/ruby/gems/2.3.0/gems/notify-0.5.2/lib/notify/ruby-growl.rb
/usr/lib64/ruby/gems/2.3.0/gems/notify-0.5.2/lib/notify/ruby_gntp.rb
/usr/lib64/ruby/gems/2.3.0/gems/notify-0.5.2/lib/notify/terminal-notifier.rb
/usr/lib64/ruby/gems/2.3.0/gems/notify-0.5.2/lib/notify/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/notify-0.5.2/notify.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/notify-0.5.2/sample.rb
/usr/lib64/ruby/gems/2.3.0/specifications/notify-0.5.2.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/notify
