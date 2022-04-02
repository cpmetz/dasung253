{
  lib,
  python3Packages
}: let
  pname = "dasung";
  version = "1.0";
in
  with python3Packages;
  buildPythonApplication {
    inherit pname version;
    buildInputs = [ pyserial ];
    propogatedBuildInputs = [ pyserial ];
    src = ./.;
  }
