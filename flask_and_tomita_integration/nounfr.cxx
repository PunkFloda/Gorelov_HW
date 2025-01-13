#encoding "utf-8"    // сообщаем парсеру о том, в какой кодировке написана грамматика
#GRAMMAR_ROOT S      // указываем корневой нетерминал грамматики
Adj_1 -> AnyWord<wff="[А-ЯЁа-яё]+(ая|яя|ой|ый|ий|ое|ее|ые|ие)",gram=~"SPRO,APRO,V,S">; 
Adj_1 -> AnyWord<wff="[А-ЯЁа-яё]+(ой|ей|ого|его|ых|их|ому|ему|ыи|им)",gram=~"SPRO,APRO,V,S">; 
Adj_1 -> AnyWord<wff="[А-ЯЁа-яё]+(ую|юю|ом|ем)",gram=~"SPRO,APRO,V">;  



S -> Noun<gnc-agr[1]> Adj_1<gnc-agr[1], gram='A'> | Adj_1<gnc-agr[1], gram='A'> Noun<gnc-agr[1]>;
//вывод в таблицу
