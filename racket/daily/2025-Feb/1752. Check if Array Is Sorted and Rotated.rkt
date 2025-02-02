(define/contract (check nums)
  (-> (listof exact-integer?) boolean?)
    (define (loop prev remaining rotated)
        (cond
            [(empty? remaining) (<= rotated 1)]
            [else
                (let ([current (first remaining)])
                    (if (< current prev)
                        (loop current (rest remaining) (add1 rotated))
                        (loop current (rest remaining) rotated)
                    )
                )
            ]
        )
    )
    (loop (first nums) (append (rest nums) (list (first nums))) 0)
)