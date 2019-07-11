WEECHAT_RC_OK = ...
WEECHAT_RC_OK_EAT = ...
WEECHAT_RC_ERROR = ...
WEECHAT_CONFIG_READ_OK = ...
WEECHAT_CONFIG_READ_MEMORY_ERROR = ...
WEECHAT_CONFIG_READ_FILE_NOT_FOUND = ...
WEECHAT_CONFIG_WRITE_OK = ...
WEECHAT_CONFIG_WRITE_ERROR = ...
WEECHAT_CONFIG_WRITE_MEMORY_ERROR = ...
WEECHAT_CONFIG_OPTION_SET_OK_CHANGED = ...
WEECHAT_CONFIG_OPTION_SET_OK_SAME_VALUE = ...
WEECHAT_CONFIG_OPTION_SET_ERROR = ...
WEECHAT_CONFIG_OPTION_SET_OPTION_NOT_FOUND = ...
WEECHAT_CONFIG_OPTION_UNSET_OK_NO_RESET = ...
WEECHAT_CONFIG_OPTION_UNSET_OK_RESET = ...
WEECHAT_CONFIG_OPTION_UNSET_OK_REMOVED = ...
WEECHAT_CONFIG_OPTION_UNSET_ERROR = ...
WEECHAT_LIST_POS_SORT = ...
WEECHAT_LIST_POS_BEGINNING = ...
WEECHAT_LIST_POS_END = ...
WEECHAT_HOTLIST_LOW = ...
WEECHAT_HOTLIST_MESSAGE = ...
WEECHAT_HOTLIST_PRIVATE = ...
WEECHAT_HOTLIST_HIGHLIGHT = ...
WEECHAT_HOOK_PROCESS_RUNNING = ...
WEECHAT_HOOK_PROCESS_ERROR = ...
WEECHAT_HOOK_CONNECT_OK = ...
WEECHAT_HOOK_CONNECT_ADDRESS_NOT_FOUND = ...
WEECHAT_HOOK_CONNECT_IP_ADDRESS_NOT_FOUND = ...
WEECHAT_HOOK_CONNECT_CONNECTION_REFUSED = ...
WEECHAT_HOOK_CONNECT_PROXY_ERROR = ...
WEECHAT_HOOK_CONNECT_LOCAL_HOSTNAME_ERROR = ...
WEECHAT_HOOK_CONNECT_GNUTLS_INIT_ERROR = ...
WEECHAT_HOOK_CONNECT_GNUTLS_HANDSHAKE_ERROR = ...
WEECHAT_HOOK_CONNECT_MEMORY_ERROR = ...
WEECHAT_HOOK_CONNECT_TIMEOUT = ...
WEECHAT_HOOK_CONNECT_SOCKET_ERROR = ...
WEECHAT_HOOK_SIGNAL_STRING = ...
WEECHAT_HOOK_SIGNAL_INT = ...
WEECHAT_HOOK_SIGNAL_POINTER = ...

def plugin_get_name(plugin): ...
def charset_set(charset): ...
def iconv_to_internal(charset, string): ...
def iconv_from_internal(charset, string): ...
def gettext(string): ...
def ngettext(string, plural, count): ...
def strlen_screen(string): ...
def string_match(string, mask, case_sensitive): ...
def string_match_list(string, masks, case_sensitive): ...
def string_eval_path_home(path, pointers, extra_vars, options): ...
def string_mask_to_regex(mask): ...
def string_has_highlight(string, highlight_words): ...
def string_has_highlight_regex(string, regex): ...
def string_format_size(size): ...
def string_remove_color(string, replacement): ...
def string_is_command_char(string): ...
def string_input_for_buffer(string): ...
def string_eval_expression(expr, pointers, extra_vars, options): ...
def mkdir_home(directory, mode): ...
def mkdir(directory, mode): ...
def mkdir_parents(directory, mode): ...
def list_new(): ...
def list_add(list, data, where, user_data): ...
def list_search(list, data): ...
def list_search_pos(list, data): ...
def list_casesearch(list, data): ...
def list_casesearch_pos(list, data): ...
def list_get(list, position): ...
def list_set(item, value): ...
def list_next(item): ...
def list_prev(item): ...
def list_string(item): ...
def list_size(list): ...
def list_remove(list, item): ...
def list_remove_all(list): ...
def list_free(list): ...
def config_new(name, callback_reload, callback_reload_data): ...
def config_new_section(config_file, name, user_can_add_options, user_can_delete_options, callback_read, callback_read_data, callback_write, callback_write_data, callback_create_option, callback_create_option_data, callback_delete_option, callback_delete_option_data): ...
def config_search_section(config_file, section_name): ...
def config_new_option(config_file, section, name, type, description, string_values, min, max, default_value, value, null_value_allowed, callback_check_value, callback_check_value_data, callback_change, callback_change_data, callback_delete, callback_delete_data): ...
def config_search_option(config_file, section, option_name): ...
def config_string_to_boolean(text): ...
def config_option_reset(option, run_callback): ...
def config_option_set(option, value, run_callback): ...
def config_option_set_null(option, run_callback): ...
def config_option_unset(option): ...
def config_option_rename(option, new_name): ...
def config_option_is_null(option): ...
def config_option_default_is_null(option): ...
def config_boolean(option): ...
def config_boolean_default(option): ...
def config_integer(option): ...
def config_integer_default(option): ...
def config_string(option): ...
def config_string_default(option): ...
def config_color(option): ...
def config_color_default(option): ...
def config_write_option(config_file, option): ...
def config_write_line(config_file, option_name, value): ...
def config_write(config_file): ...
def config_read(config_file): ...
def config_reload(config_file): ...
def config_option_free(option): ...
def config_section_free_options(section): ...
def config_section_free(section): ...
def config_free(config_file): ...
def config_get(option_name): ...
def config_get_plugin(option_name): ...
def config_is_set_plugin(option_name): ...
def config_set_plugin(option_name, value): ...
def config_set_desc_plugin(option_name, description): ...
def config_unset_plugin(option_name): ...
def key_bind(context, keys): ...
def key_unbind(context, key): ...
def prefix(prefix): ...
def color(color_name): ...
def prnt(buffer, message): ...
def prnt_date_tags(buffer, date, tags, message): ...
def prnt_y(buffer, y, message): ...
def log_print(message): ...
def hook_command(command, description, args, args_description, completion, callback, callback_data): ...
def hook_completion(completion_item, description, callback, callback_data): ...
def hook_completion_get_string(completion, property): ...
def hook_completion_list_add(completion, word, nick_completion, where): ...
def hook_command_run(command, callback, callback_data): ...
def hook_timer(interval, align_second, max_calls, callback, callback_data): ...
def hook_fd(fd, flag_read, flag_write, flag_exception, callback, callback_data): ...
def hook_process(command, timeout, callback, callback_data): ...
def hook_process_hashtable(command, options, timeout, callback, callback_data): ...
def hook_connect(proxy, address, port, ipv6, retry, local_hostname, callback, callback_data): ...
def hook_line(buffer_type, buffer_name, tags, callback, callback_data): ...
def hook_print(buffer, tags, message, strip_colors, callback, callback_data): ...
def hook_signal(signal, callback, callback_data): ...
def hook_signal_send(signal, type_data, signal_data): ...
def hook_hsignal(signal, callback, callback_data): ...
def hook_hsignal_send(signal, hashtable): ...
def hook_config(option, callback, callback_data): ...
def hook_modifier(modifier, callback, callback_data): ...
def hook_modifier_exec(modifier, modifier_data, string): ...
def hook_info(info_name, description, args_description, callback, callback_data): ...
def hook_info_hashtable(info_name, description, args_description, output_description, callback, callback_data): ...
def hook_infolist(infolist_name, description, pointer_description, args_description, callback, callback_data): ...
def hook_focus(area, callback, callback_data): ...
def hook_set(hook, property, value): ...
def unhook(hook): ...
def unhook_all(): ...
def buffer_new(name, input_callback, input_callback_data, close_callback, close_callback_data): ...
def current_buffer(): ...
def buffer_search(plugin, name): ...
def buffer_search_main(): ...
def buffer_clear(buffer): ...
def buffer_close(buffer): ...
def buffer_merge(buffer, target_buffer): ...
def buffer_unmerge(buffer, number): ...
def buffer_get_integer(buffer, property): ...
def buffer_get_string(buffer, property): ...
def buffer_get_pointer(buffer, property): ...
def buffer_set(buffer, property, value): ...
def buffer_string_replace_local_var(buffer, string): ...
def buffer_match_list(buffer, string): ...
def current_window(): ...
def window_search_with_buffer(buffer): ...
def window_get_integer(window, property): ...
def window_get_pointer(window, property): ...
def window_set_title(window, title): ...
def nicklist_add_group(buffer, parent_group, name, color, visible): ...
def nicklist_search_group(buffer, from_group, name): ...
def nicklist_add_nick(buffer, group, name, color, prefix, prefix_color, visible): ...
def nicklist_search_nick(buffer, from_group, name): ...
def nicklist_remove_group(buffer, group): ...
def nicklist_remove_nick(buffer, nick): ...
def nicklist_remove_all(buffer): ...
def nicklist_group_get_integer(buffer, group, property): ...
def nicklist_group_get_string(buffer, group, property): ...
def nicklist_group_get_pointer(buffer, group, property): ...
def nicklist_group_set(buffer, group, property, value): ...
def nicklist_nick_get_integer(buffer, nick, property): ...
def nicklist_nick_get_string(buffer, nick, property): ...
def nicklist_nick_get_pointer(buffer, nick, property): ...
def nicklist_nick_set(buffer, nick, property, value): ...
def bar_item_search(name): ...
def bar_item_new(name, build_callback, build_callback_data): ...
def bar_item_update(name): ...
def bar_item_remove(item): ...
def bar_search(name): ...
def bar_new(name, hidden, priority, type, condition, position, filling_top_bottom, filling_left_right, size, size_max, color_fg, color_delim, color_bg, separator, items): ...
def bar_set(bar, property, value): ...
def bar_update(name): ...
def bar_remove(bar): ...
def command(buffer, command): ...
def command_options(buffer, command, options): ...
def info_get(info_name, arguments): ...
def info_get_hashtable(info_name, dict_in): ...
def infolist_new(): ...
def infolist_new_item(infolist): ...
def infolist_new_var_integer(item, name, value): ...
def infolist_new_var_string(item, name, value): ...
def infolist_new_var_pointer(item, name, pointer): ...
def infolist_new_var_time(item, name, time): ...
def infolist_get(infolist_name, pointer, arguments): ...
def infolist_next(infolist): ...
def infolist_prev(infolist): ...
def infolist_reset_item_cursor(infolist): ...
def infolist_search_var(infolist, name): ...
def infolist_fields(infolist): ...
def infolist_integer(infolist, var): ...
def infolist_string(infolist, var): ...
def infolist_pointer(infolist, var): ...
def infolist_time(infolist, var): ...
def infolist_free(infolist): ...
def hdata_get(hdata_name): ...
def hdata_get_var_offset(hdata, name): ...
def hdata_get_var_type_string(hdata, name): ...
def hdata_get_var_array_size(hdata, pointer, name): ...
def hdata_get_var_array_size_string(hdata, pointer, name): ...
def hdata_get_var_hdata(hdata, name): ...
def hdata_get_list(hdata, name): ...
def hdata_check_pointer(hdata, list, pointer): ...
def hdata_move(hdata, pointer, count): ...
def hdata_search(hdata, pointer, search, count): ...
def hdata_char(hdata, pointer, name): ...
def hdata_integer(hdata, pointer, name): ...
def hdata_long(hdata, pointer, name): ...
def hdata_string(hdata, pointer, name): ...
def hdata_pointer(hdata, pointer, name): ...
def hdata_time(hdata, pointer, name): ...
def hdata_hashtable(hdata, pointer, name): ...
def hdata_compare(hdata, pointer1, pointer2, name, case_sensitive): ...
def hdata_update(hdata, pointer, hashtable): ...
def hdata_get_string(hdata, property): ...
def upgrade_new(filename, callback_read, callback_read_data): ...
def upgrade_write_object(upgrade_file, object_id, infolist): ...
def upgrade_read(upgrade_file): ...
def upgrade_close(upgrade_file): ...
def register(name, author, version, license, description, shutdown_function, charset): ...
def window_get_string(window, property): ...
