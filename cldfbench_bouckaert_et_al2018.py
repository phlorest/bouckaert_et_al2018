import pathlib

import phlorest
from tqdm import tqdm


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "bouckaert_et_al2018"

    def cmd_makecldf(self, args):
        self.init(args)
        with self.nexus_summary() as nex:
            self.add_tree_from_nexus(
                args,
                self.raw_dir / '41559_2018_489_MOESM4_ESM.txt',
                nex,
                'summary',
            )
        posterior = self.sample(
            self.read_gzipped_text(self.raw_dir / 'pny10.fixed.cov.ucln.bdsky.ba-sp.trees.gz'),
            detranslate=True,
            as_nexus=True)

        with self.nexus_posterior() as nex:
            for i, tree in tqdm(enumerate(posterior.trees.trees, start=1), total=1000):
                self.add_tree(args, tree, nex, 'posterior-{}'.format(i))

        self.add_data(args, phlorest.BeastFile(self.raw_dir / '41559_2018_489_MOESM3_ESM.xml'))
