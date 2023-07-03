func solution(_ num:Int) -> Int {
    
    func find(_ num :Int, _ count: Int = 0) -> Int {
        if num == 1 { return count}
        if count == 500 { return -1}
        
        if num % 2 == 0 {
            return find(num / 2, count + 1)
        } else {
            return find(num * 3 + 1, count + 1)
        }
        
        
    }
    

    
    return find(num)
}
