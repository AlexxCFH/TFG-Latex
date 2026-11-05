# Compilar con: latexmk -pdf main.tex   (o Latexmk desde TeXstudio)
$pdf_mode = 1;
$bibtex_use = 2;   # usa biber automáticamente

# Regla para el glosario y los acrónimos (makeglossaries)
add_cus_dep('glo', 'gls', 0, 'makeglossaries');
add_cus_dep('acn', 'acr', 0, 'makeglossaries');
sub makeglossaries {
    my ($base_name, $path) = fileparse($_[0]);
    pushd $path;
    my $return = system "makeglossaries", $base_name;
    popd;
    return $return;
}
push @generated_exts, 'glo', 'gls', 'glg', 'acn', 'acr', 'alg', 'ist', 'lol';
