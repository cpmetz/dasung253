_: super: {
  python3 = super.python3.override {
    packageOverrides = pyself: _: {
      dasung = pyself.callPackage ./derivation.nix {};
    };
  };
}
