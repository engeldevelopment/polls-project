from page_objects import PageObject, PageElement


class HomePage(PageObject):
	link_to_result = PageElement(css='a[data-result]')
	link_to_poll = PageElement(css='a[data-encuesta]')
	poll_title = PageElement(tag_name='h4')
	message = PageElement(css='h4[data-message')


class PollPage(PageObject):
	btn_vote = PageElement(id_='btn-votar')
	link_to_back = PageElement(tag_name='a')
	message = PageElement(css='p[data-msj]')
	title = PageElement(css='h2.card-title')
	options = PageElement(css='input[type="radio"')


class ResultPage(PageObject):
	title = PageElement(css='h2.card-title')
	subtitle = PageElement(tag_name='h4')
	message = PageElement(css='p[data-error')
	link_to_back = PageElement(tag_name='a')
