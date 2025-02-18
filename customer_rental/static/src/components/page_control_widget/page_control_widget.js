/** @odoo-module **/

import { registry } from '@web/core/registry';


const { Component, useState } = owl;

export class pageControlWidget extends Component {
    setup() {
        super.setup();
        this.state = useState({page_number : 1});
    }
    clickNext() {
        const totalTabs = document.querySelectorAll('li.nav-item').length;
        console.log("Type of Page number: ", typeof this.state.page_number)
        console.log("Type of Page number: ", typeof totalTabs)
        if (this.state.page_number < totalTabs) {
            const nextTab = document.querySelector(`li.nav-item:nth-child(${this.state.page_number + 1}) a`);
            if (nextTab) {
                this.state.page_number += 1;
                nextTab.click();
            }
        }
    }

    clickPrevious() {
    if (this.state.page_number > 1) {
        const previousTab = document.querySelector(`li.nav-item:nth-child(${this.state.page_number - 1}) a`);
        if (previousTab) {
            this.state.page_number -= 1;
            previousTab.click();
        }
    }
}

}
pageControlWidget.template = `pageControlWidget`;

registry.category('view_widgets').add('page_control_widget', pageControlWidget);