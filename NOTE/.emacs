(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(column-number-mode t)
 '(display-time-mode t)
 '(tool-bar-mode nil)
 '(menu-bar-mode nil))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )


(if window-system
        (setq default-frame-alist
                (append
                        '( (top . 80)
                                 (left . 100)
                                             (width . 110)
                                             (height . 35))
                                                                  default-frame-alist))
)

;; load .emacsd/*.el and use color-theme plugin
(setq load-path (cons "~/.emacs.d" load-path))
(require 'color-theme)
(color-theme-initialize)
(color-theme-dark-blue2)

;; For my language code setting (UTF-8)
;;(setq current-language-environment 'UTF-8)
;;(setq default-input-method "chinese-py")
;;(setq locale-coding-system 'utf-8)
;;(set-terminal-coding-system 'utf-8)
;;(set-keyboard-coding-system 'utf-8)
;;(set-selection-coding-system 'utf-8)
;;(prefer-coding-system 'utf-8)
;; utf8 with default-coding-system and new 
(setq default-buffer-file-coding-system 'utf-8)
;;Default coding system (for new files) 

;; highlight marked region
(transient-mark-mode t)

;; enable syntax highlight
(global-font-lock-mode t)

;;emacs clipboard
(setq x-select-enable-clipboard t)

;; display time config
(display-time-mode t)
(setq display-time-24hr-format t)
(setq display-time-day-and-date nil)
(setq display-time-interval 60)

;; use F10 to show/hidden menu-bar
(global-set-key [(f10)] 'menu-bar-mode)

(global-linum-mode 1)
(setq column-number-mode t)

(setq auto-save-mode t)


(setq frame-title-format "%b@ASUS-PC")

(setq default-fill-column 80)
(icomplete-mode 1)
(blink-cursor-mode -1)

;; backup config
(setq version-control t)
(setq kept-old-versions 2)
(setq kept-new-versions 5)
(setq delete-old-versions t)
(setq backup-directory-alist '(("." . "~/.emacs.d/backup")))
(setq backup-by-copying t)
(setq make-backup-files nil)
(global-auto-revert-mode 1)

(mouse-avoidance-mode 'animate)

(setq make-backup-file nil)

(setq require-final-newline t)

(setq auto-image-file-mode t)

(setq echo-keystrokes 0.1)

(setq default-fill-column 80)

(setq user-full-name "ifconfigyeah")
(setq user-mail-address "ifconfig@yeah.net")

(global-set-key [?\C-\M-g] 'goto-line)


