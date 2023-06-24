func solution(_ s:String) -> String {
    var index: Int = -1
    return s.map {
        index += 1
        if $0 == " " {
            index = -1
            return String($0)
        } else if index % 2 == 0 {
            return String($0.uppercased())
        } else {
            return String($0.lowercased())
        }
    }.joined()
}
