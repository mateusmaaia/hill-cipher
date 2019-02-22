package main

import (
	"fmt"
	"gonum.org/v1/gonum/mat"
)

func main() {
	const encryptedString string = "S Ţ Õ V ŝ Ø O ƙ ó M Ţ Ï E Ű á"
	decrptMatrix := mat.NewDense(3, 3, []float64{1,0,0,
												1,3,1,
												1,2,0})
	
	var inversedMatrix mat.Dense
	inversedMatrix.Inverse(decrptMatrix)
	fmt.Println(inversedMatrix)

	// fmt.Println(reflect.TypeOf(inversedMatrix))

}
