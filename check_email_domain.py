default_install_hook_types:
 [pre-commit]



repos:
 - repo: https://github.com/macisamuele/language-formatters-pre-commit-hooks
   rev: v2.12.0
   hooks:
     - id: pretty-format-java
       args: [--autofix, --google-java-formatter-version=1.21.0]



 - repo: local
   hooks:
     - id: check_commiter_email_id
       name: check commiter email id
       entry : python3 check_mail_domain.py
       language: python
       stages: [commit-msg]