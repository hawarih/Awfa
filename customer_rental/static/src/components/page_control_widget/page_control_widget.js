/** @odoo-module **/

import { registry } from '@web/core/registry';


const { Component, useState } = owl;

export class pageControlWidget extends Component {
    setup() {
        super.setup();
        this.state = useState({page_number : 1});
    }
    clickNext(){
        this.state.page_number += 1;
        $('li.nav-item:nth-child(' + this.state.page_number + ') a').get(0).click();
    }
    clickPrevious(){
        this.state.page_number -= 1;
        $('li.nav-item:nth-child(' + this.state.page_number + ') a').get(0).click();
    }

}
pageControlWidget.template = `pageControlWidget`;

registry.category('view_widgets').add('page_control_widget', pageControlWidget);