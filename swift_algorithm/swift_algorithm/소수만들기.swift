import Foundation


func solution(_ nums:[Int]) -> Int {
    var answer = 0

    func combination(_ count: Int = 0, _ total:Int = 0, _ start:Int = 0) {
        if count == 3 {
            var i = 2
            while i * i <= total {
                if total % i == 0 {
                    return
                }
                i += 1
            }

            answer += 1
            return
        }

        for i in start..<nums.count{
            combination(count + 1, total + nums[i], i + 1)
        }
    }
    
    combination()


    return answer == 0 ? -1 : answer
}
