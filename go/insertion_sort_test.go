package sorting

import (
	"reflect"
	"testing"
)

func TestSort_Empty(t *testing.T) {

	seq := make([]int, 1)

	r := seq.ins_sort()

	eq := reflect.DeepEqual(r, seq)

	if eq == false {
		t.Error("Empty list is empty even when sorted")
	}
}

func TestSort_One(t *testing.T) {

	seq := []int{2}

	r := seq.ins_sort()

	eq := reflect.DeepEqual([]int{2}, r)

	if eq == false {
		t.Error("[2] must be equal to istself")
	}
}

func TestSort_List(t *testing.T) {

	seq := []int{4, 3, 2, 1}

	r := seq.ins_sort()

	eq := reflect.DeepEqual([]int{1, 2, 3, 4}, r)

	if eq == false {
		t.Error("Soreted list are not equals")
	}
}
