rule sensitive_keyword {
    strings:
        $keyword = "sensible"
    condition:
        $keyword
}
