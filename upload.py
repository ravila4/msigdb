import biothings.hub.dataload.uploader as uploader
from .parser import load_data


class msigdbUploader(uploader.BaseSourceUploader):

    name = "msigdb"
    __metadata__ = {
        "src_meta": {
            'license_url': 'https://www.gsea-msigdb.org/gsea/msigdb_license_terms.jsp',
            'licence': 'CC Attribution 4.0 International',
            'url': 'https://www.gsea-msigdb.org/gsea/index.jsp'
            }
        }

    def load_data(self, data_folder):
        self.logger.info("Load data from folder '%s'" % data_folder)
        msigdb_docs = load_data(data_folder)
        return msigdb_docs
