package sorting

func (seq []int) ins_sort() []int {

	for j, _ := range seq {
		for {
			if j > 0 && seq[j-1] > seq[j] {
				seq[j-1], seq[j] = seq[j], seq[j-1]
				j = j - 1
			} else {
				break
			}
		}
	}

	return seq
}

func (seq []string) ins_sort() []string {
	var ret string = "TODO"
	return ret
}
