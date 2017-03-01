import { PanchayatPage } from './app.po';

describe('panchayat App', () => {
  let page: PanchayatPage;

  beforeEach(() => {
    page = new PanchayatPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
