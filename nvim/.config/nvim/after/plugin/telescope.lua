local builtin = require('telescope.builtin')
vim.keymap.set('n', '<leader>pa', builtin.find_files, {})
vim.keymap.set('n', '<leader>pg', builtin.git_files, {})