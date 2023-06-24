func solution(_ x:Int, _ n:Int) -> [Int64] {
    return stride(from:x, through: x*n , by:x).map { Int64($0) }
    
}
