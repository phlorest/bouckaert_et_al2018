import pathlib

import nexus
from pydplace import phlorest
from tqdm import tqdm


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "bouckaert_et_al2018"

    def cmd_makecldf(self, args):
        self.init(args)
        with self.nexus_summary() as nex:
            self.add_tree(
                args,
                self.read_tree(self.raw_dir / '41559_2018_489_MOESM4_ESM.txt'),
                nex,
                'summary',
            )
        posterior = self.raw_dir / 'pny10.fixed.cov.ucln.bdsky.ba-sp.trees.gz'
        posterior = nexus.NexusReader.from_string(
            self.sample(self.read_gzipped_text(posterior), detranslate=True))

        with self.nexus_posterior() as nex:
            for i, tree in tqdm(enumerate(posterior.trees.trees, start=1), total=1000):
                self.add_tree(args, tree, nex, 'posterior-{}'.format(i))

        self.add_data(args, phlorest.beast_to_nexus(self.raw_dir / '41559_2018_489_MOESM3_ESM.xml'))
