(add-to-list 'default-frame-alist
	     '(font . "JetBrainsMono Nerd Font-14"))
(setq make-backup-files nil)
(setq auto-save-default nil)
(setq inhibit-startup-screen t)
(add-hook 'window-setup-hook 'toggle-frame-maximized t)

(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)

(setq package-selected-packages '(evil doom-themes spacemacs-theme monokai-theme yasnippet which-key flycheck lsp-ui lsp-mode company atom-one-dark-theme))

(when (cl-find-if-not #'package-installed-p package-selected-packages)
  (package-refresh-contents)
  (mapc #'package-install package-selected-packages))

;; =============================================================================
(require 'evil)
(evil-mode 1)
(evil-set-leader 'normal (kbd "SPC"))
(evil-define-key 'normal 'global (kbd "<leader>s") 'save-buffer)
(evil-define-key 'normal 'global (kbd "<leader>c") 'save-buffers-kill-emacs)
(evil-define-key 'normal 'global (kbd "<leader>d") 'dired-jump)
(evil-define-key 'normal 'global (kbd "<leader>f") 'find-file)
(evil-define-key 'normal 'global (kbd "<leader>b") 'switch-to-buffer)
(evil-define-key 'normal 'global (kbd "<leader>wo") 'delete-other-windows)
(evil-define-key 'normal 'global (kbd "<leader>wv") 'split-window-right)
(evil-define-key 'normal 'global (kbd "<leader>wn") 'split-window-below)
(evil-define-key 'normal 'global (kbd "<leader>wc") 'delete-window)
(evil-define-key 'normal 'global (kbd "<leader>ww") 'evil-window-next)
(evil-define-key 'normal 'global (kbd "<leader>wh") 'evil-window-left)
(evil-define-key 'normal 'global (kbd "<leader>wj") 'evil-window-down)
(evil-define-key 'normal 'global (kbd "<leader>wk") 'evil-window-up)
(evil-define-key 'normal 'global (kbd "<leader>wl") 'evil-window-right)
(evil-define-key 'normal 'global (kbd "<leader>w=") 'balance-windows)

;; (global-set-key (kbd "M-x") #'helm-M-x)
;; (global-set-key (kbd "C-x r b") #'helm-filtered-bookmarks)
;; (global-set-key (kbd "C-x C-f") #'helm-find-files)
;; (helm-mode 1)

(require 'lsp-mode)
(setq lsp-signature-render-documentation nil)
(add-hook 'c-mode-hook #'lsp)
(add-hook 'c++-mode-hook #'lsp)

(add-hook 'after-init-hook 'global-company-mode)
(setq company-icon-size 28)
(setq company-idle-delay 0)
(setq company-minimum-prefix-length 1)
(setq lsp-idle-delay 0.1)
(setq company-tooltip-align-annotations t)
(with-eval-after-load 'company
  (define-key company-active-map (kbd "<tab>") #'company-select-next))
(with-eval-after-load 'company
  (define-key company-active-map (kbd "<backtab>") #'company-select-previous))

(yas-reload-all)
(add-hook 'prog-mode-hook #'yas-minor-mode)

(global-flycheck-mode)
(add-hook 'after-init-hook #'global-flycheck-mode)
(require 'which-key)
(which-key-mode)

(load-theme 'atom-one-dark t)
;; ============================================================================
