vim.opt.list = true
vim.opt.listchars:append "eol:↴"
vim.cmd [[highlight IndentBlanklineChar guifg=#7d7c7c gui=nocombine]]
require("indent_blankline").setup {
    space_char_blankline = " ",
    show_current_context = true,
    show_current_context_start = true,
    use_treesitter = true,
}
