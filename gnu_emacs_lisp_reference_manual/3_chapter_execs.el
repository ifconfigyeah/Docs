;;;"3_chapter_execs.el"

;;;Write a non-interactive function that doubles the value of its argument, a number.

(defun tmp_double_value (number)
  "Return doubles of NUMBER"
  (+ number number))

(tmp_double_value 5) ; print 10


;;;Make that function interactive.
(defun tmp_double_value2 (number)  ;Interactive version
  "Return doubles of NUMBER"
  (interactive "p")
  (message "The result is %d" (* 2 number)))

(tmp_double_value2 6)  ;print "The result is 12"

;;; Write a function that tests whether the current value of `fill-column' is greater than the argument passed to the function, and if so, prints an appropriate message.

(defun tmp_is_argument_lesser_than_fill-column (number)
  "Test the NUMBER is lesser than fill-column"
  (interactive "p")
  (if (< number fill-column)
      (message "The arg is lesser than fill-column.")
    (message "The arg is not lesser than fill-column")))

(tmp_is_argument_lesser_than_fill-column 70)


(defun tmp_is_argument_lesser_than_fill-column2 (number)   ;; version 2, can not work now
  "Test the NUMBER is lesser than fill-column"
  (interactive "p")
  (if (equal number fill-column)
      (message "The arg is equal fill-column")
    (if (< number fill-column))
    (message "The arg is lesser than fill-column")
    (message "The arg is greater than fill-column")))

(tmp_is_argument_lesser_than_fill-column2 2)



