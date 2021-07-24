%global fontname gfs-olga
%global fontconf 61-%{fontname}.conf

%global archivename GFS_OLGA_OT

Name:    %{fontname}-fonts
Version: 20060908
Release: 26%{?dist}
Summary: GFS Olga experimental oblique font

License:   OFL
URL:       http://www.greekfontsociety.gr/pages/en_typefaces20th.html
Source0:   http://www.greekfontsociety.gr/%{archivename}.zip
Source1:   %{name}-fontconfig.conf
Source2:   %{fontname}.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
In Greece the terms italic and oblique have the same meaning since they are
borrowed from the latin typographic practice without any real historical
equivalent in Greek history. Until the end of the 19th century Greek typefaces
were cut and cast indepedently, not as members of a typefamily. The
mechanisation of typecutting allowed the transformation of upright Greek
typefaces to oblique designs. Nonetheless, the typesetting practice of a
cursive Greek font to complement an upright one did not survive the 19th
century.

The experimental font GFS Olga (1995) attempts to revive this lost tradition.
The typeface was designed and digitised by George Matthiopoulos, based on the
historical Porson Greek type (1803) with the intention to be the companion of
the upright GFS Didot font whenever there is a need for an italic alternative.


%prep
%setup -q -c -T
unzip -j -L -q %{SOURCE0}
chmod 0644 *.txt
for txt in *.txt ; do
   fold -s $txt > $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.otf
%doc *.txt *.pdf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20060908-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20060908-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20060908-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20060908-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20060908-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20060908-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20060908-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Parag Nemade <pnemade AT redhat DOT com> - 20060908-18
- Add metainfo file to show this font in gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060908-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20060908-9
— prepare for F11 mass rebuild, new rpm and new fontpackages

* Sun Nov 23 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20060908-8
ᛤ ‘rpm-fonts’ renamed to “fontpackages”

* Fri Nov 14 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20060908-7
▤ Rebuild using new « rpm-fonts »

* Fri Jul 11 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20060908-6
⌖ Fedora 10 alpha general package cleanup

* Wed Apr 30 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20060908-5
⥁ Yet another prep fix®

* Mon Mar 17 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20060908-4
⚰ RIP OSX zip metadata. You won't be missed.

* Sun Feb 17 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20060908-2
⌂ Update URL

* Sun Nov 25 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
☺ 20060908-1
✓ initial packaging