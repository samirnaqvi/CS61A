(define (find s predicate)
(if (null? s)
      #f
      (if (predicate (car s))
          (car s) 
          (find (cdr-stream s) predicate ))))



(define (scale-stream s k)
  (cons-stream (*(car s)k)
  	(scale-stream (cdr-stream s) k))
)

(define (has-cycle s)


	(define (helper y b)
	
			
	(if (or (null? y) (null?  (cdr-stream y))(null?  (cdr-stream b))(null?  b))
      #f
      (if (eq? y b)
          #t
          (helper (cdr-stream y) (cdr-stream(cdr-stream b)) )))
		)

	(helper s (cdr-stream s)
	)
	)
(define (has-cycle-constant s)
  
)
